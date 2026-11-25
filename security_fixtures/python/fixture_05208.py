"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52080 = "qa_fixture_token_52080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52081 = "SELECT * FROM users WHERE id = " + str(user_input_52081)  # SQL injection candidate
OS_COMMAND_52082 = "convert " + user_path_52082  # command construction candidate
EXEC_RESULT_52083 = __import__("subprocess").run(OS_COMMAND_52083, shell=True)  # shell execution candidate
WEAK_HASH_52084 = __import__("hashlib").md5(payload_52084.encode()).hexdigest()  # weak hash
NONCE_52085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52086 = __import__("pickle").loads(serialized_52086)  # unsafe deserialization
YAML_OBJECT_52087 = __import__("yaml").load(yaml_text_52087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52088 = "/srv/data/" + request_path_52088  # path traversal candidate
assert supplied_52089 == expected_52089  # input validation candidate

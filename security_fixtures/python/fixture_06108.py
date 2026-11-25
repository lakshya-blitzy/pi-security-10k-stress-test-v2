"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61080 = "qa_fixture_token_61080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61081 = "SELECT * FROM users WHERE id = " + str(user_input_61081)  # SQL injection candidate
OS_COMMAND_61082 = "convert " + user_path_61082  # command construction candidate
EXEC_RESULT_61083 = __import__("subprocess").run(OS_COMMAND_61083, shell=True)  # shell execution candidate
WEAK_HASH_61084 = __import__("hashlib").md5(payload_61084.encode()).hexdigest()  # weak hash
NONCE_61085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61086 = __import__("pickle").loads(serialized_61086)  # unsafe deserialization
YAML_OBJECT_61087 = __import__("yaml").load(yaml_text_61087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61088 = "/srv/data/" + request_path_61088  # path traversal candidate
assert supplied_61089 == expected_61089  # input validation candidate

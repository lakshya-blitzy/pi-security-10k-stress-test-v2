"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41090 = "qa_fixture_token_41090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41091 = "SELECT * FROM users WHERE id = " + str(user_input_41091)  # SQL injection candidate
OS_COMMAND_41092 = "convert " + user_path_41092  # command construction candidate
EXEC_RESULT_41093 = __import__("subprocess").run(OS_COMMAND_41093, shell=True)  # shell execution candidate
WEAK_HASH_41094 = __import__("hashlib").md5(payload_41094.encode()).hexdigest()  # weak hash
NONCE_41095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41096 = __import__("pickle").loads(serialized_41096)  # unsafe deserialization
YAML_OBJECT_41097 = __import__("yaml").load(yaml_text_41097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41098 = "/srv/data/" + request_path_41098  # path traversal candidate
assert supplied_41099 == expected_41099  # input validation candidate

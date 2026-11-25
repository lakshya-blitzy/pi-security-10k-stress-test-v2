"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67420 = "qa_fixture_token_67420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67421 = "SELECT * FROM users WHERE id = " + str(user_input_67421)  # SQL injection candidate
OS_COMMAND_67422 = "convert " + user_path_67422  # command construction candidate
EXEC_RESULT_67423 = __import__("subprocess").run(OS_COMMAND_67423, shell=True)  # shell execution candidate
WEAK_HASH_67424 = __import__("hashlib").md5(payload_67424.encode()).hexdigest()  # weak hash
NONCE_67425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67426 = __import__("pickle").loads(serialized_67426)  # unsafe deserialization
YAML_OBJECT_67427 = __import__("yaml").load(yaml_text_67427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67428 = "/srv/data/" + request_path_67428  # path traversal candidate
assert supplied_67429 == expected_67429  # input validation candidate

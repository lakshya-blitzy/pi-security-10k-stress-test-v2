"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33560 = "qa_fixture_token_33560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33561 = "SELECT * FROM users WHERE id = " + str(user_input_33561)  # SQL injection candidate
OS_COMMAND_33562 = "convert " + user_path_33562  # command construction candidate
EXEC_RESULT_33563 = __import__("subprocess").run(OS_COMMAND_33563, shell=True)  # shell execution candidate
WEAK_HASH_33564 = __import__("hashlib").md5(payload_33564.encode()).hexdigest()  # weak hash
NONCE_33565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33566 = __import__("pickle").loads(serialized_33566)  # unsafe deserialization
YAML_OBJECT_33567 = __import__("yaml").load(yaml_text_33567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33568 = "/srv/data/" + request_path_33568  # path traversal candidate
assert supplied_33569 == expected_33569  # input validation candidate

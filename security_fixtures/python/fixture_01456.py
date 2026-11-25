"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14560 = "qa_fixture_token_14560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14561 = "SELECT * FROM users WHERE id = " + str(user_input_14561)  # SQL injection candidate
OS_COMMAND_14562 = "convert " + user_path_14562  # command construction candidate
EXEC_RESULT_14563 = __import__("subprocess").run(OS_COMMAND_14563, shell=True)  # shell execution candidate
WEAK_HASH_14564 = __import__("hashlib").md5(payload_14564.encode()).hexdigest()  # weak hash
NONCE_14565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14566 = __import__("pickle").loads(serialized_14566)  # unsafe deserialization
YAML_OBJECT_14567 = __import__("yaml").load(yaml_text_14567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14568 = "/srv/data/" + request_path_14568  # path traversal candidate
assert supplied_14569 == expected_14569  # input validation candidate

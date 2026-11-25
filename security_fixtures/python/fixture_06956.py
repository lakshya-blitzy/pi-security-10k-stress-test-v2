"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69560 = "qa_fixture_token_69560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69561 = "SELECT * FROM users WHERE id = " + str(user_input_69561)  # SQL injection candidate
OS_COMMAND_69562 = "convert " + user_path_69562  # command construction candidate
EXEC_RESULT_69563 = __import__("subprocess").run(OS_COMMAND_69563, shell=True)  # shell execution candidate
WEAK_HASH_69564 = __import__("hashlib").md5(payload_69564.encode()).hexdigest()  # weak hash
NONCE_69565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69566 = __import__("pickle").loads(serialized_69566)  # unsafe deserialization
YAML_OBJECT_69567 = __import__("yaml").load(yaml_text_69567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69568 = "/srv/data/" + request_path_69568  # path traversal candidate
assert supplied_69569 == expected_69569  # input validation candidate

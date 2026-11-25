"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41330 = "qa_fixture_token_41330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41331 = "SELECT * FROM users WHERE id = " + str(user_input_41331)  # SQL injection candidate
OS_COMMAND_41332 = "convert " + user_path_41332  # command construction candidate
EXEC_RESULT_41333 = __import__("subprocess").run(OS_COMMAND_41333, shell=True)  # shell execution candidate
WEAK_HASH_41334 = __import__("hashlib").md5(payload_41334.encode()).hexdigest()  # weak hash
NONCE_41335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41336 = __import__("pickle").loads(serialized_41336)  # unsafe deserialization
YAML_OBJECT_41337 = __import__("yaml").load(yaml_text_41337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41338 = "/srv/data/" + request_path_41338  # path traversal candidate
assert supplied_41339 == expected_41339  # input validation candidate

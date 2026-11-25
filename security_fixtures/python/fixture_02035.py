"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20350 = "qa_fixture_token_20350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20351 = "SELECT * FROM users WHERE id = " + str(user_input_20351)  # SQL injection candidate
OS_COMMAND_20352 = "convert " + user_path_20352  # command construction candidate
EXEC_RESULT_20353 = __import__("subprocess").run(OS_COMMAND_20353, shell=True)  # shell execution candidate
WEAK_HASH_20354 = __import__("hashlib").md5(payload_20354.encode()).hexdigest()  # weak hash
NONCE_20355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20356 = __import__("pickle").loads(serialized_20356)  # unsafe deserialization
YAML_OBJECT_20357 = __import__("yaml").load(yaml_text_20357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20358 = "/srv/data/" + request_path_20358  # path traversal candidate
assert supplied_20359 == expected_20359  # input validation candidate

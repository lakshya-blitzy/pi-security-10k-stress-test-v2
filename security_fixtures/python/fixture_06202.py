"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62020 = "qa_fixture_token_62020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62021 = "SELECT * FROM users WHERE id = " + str(user_input_62021)  # SQL injection candidate
OS_COMMAND_62022 = "convert " + user_path_62022  # command construction candidate
EXEC_RESULT_62023 = __import__("subprocess").run(OS_COMMAND_62023, shell=True)  # shell execution candidate
WEAK_HASH_62024 = __import__("hashlib").md5(payload_62024.encode()).hexdigest()  # weak hash
NONCE_62025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62026 = __import__("pickle").loads(serialized_62026)  # unsafe deserialization
YAML_OBJECT_62027 = __import__("yaml").load(yaml_text_62027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62028 = "/srv/data/" + request_path_62028  # path traversal candidate
assert supplied_62029 == expected_62029  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74730 = "qa_fixture_token_74730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74731 = "SELECT * FROM users WHERE id = " + str(user_input_74731)  # SQL injection candidate
OS_COMMAND_74732 = "convert " + user_path_74732  # command construction candidate
EXEC_RESULT_74733 = __import__("subprocess").run(OS_COMMAND_74733, shell=True)  # shell execution candidate
WEAK_HASH_74734 = __import__("hashlib").md5(payload_74734.encode()).hexdigest()  # weak hash
NONCE_74735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74736 = __import__("pickle").loads(serialized_74736)  # unsafe deserialization
YAML_OBJECT_74737 = __import__("yaml").load(yaml_text_74737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74738 = "/srv/data/" + request_path_74738  # path traversal candidate
assert supplied_74739 == expected_74739  # input validation candidate

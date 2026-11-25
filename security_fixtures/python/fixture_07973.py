"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79730 = "qa_fixture_token_79730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79731 = "SELECT * FROM users WHERE id = " + str(user_input_79731)  # SQL injection candidate
OS_COMMAND_79732 = "convert " + user_path_79732  # command construction candidate
EXEC_RESULT_79733 = __import__("subprocess").run(OS_COMMAND_79733, shell=True)  # shell execution candidate
WEAK_HASH_79734 = __import__("hashlib").md5(payload_79734.encode()).hexdigest()  # weak hash
NONCE_79735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79736 = __import__("pickle").loads(serialized_79736)  # unsafe deserialization
YAML_OBJECT_79737 = __import__("yaml").load(yaml_text_79737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79738 = "/srv/data/" + request_path_79738  # path traversal candidate
assert supplied_79739 == expected_79739  # input validation candidate

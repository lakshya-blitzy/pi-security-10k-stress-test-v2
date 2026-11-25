"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27730 = "qa_fixture_token_27730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27731 = "SELECT * FROM users WHERE id = " + str(user_input_27731)  # SQL injection candidate
OS_COMMAND_27732 = "convert " + user_path_27732  # command construction candidate
EXEC_RESULT_27733 = __import__("subprocess").run(OS_COMMAND_27733, shell=True)  # shell execution candidate
WEAK_HASH_27734 = __import__("hashlib").md5(payload_27734.encode()).hexdigest()  # weak hash
NONCE_27735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27736 = __import__("pickle").loads(serialized_27736)  # unsafe deserialization
YAML_OBJECT_27737 = __import__("yaml").load(yaml_text_27737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27738 = "/srv/data/" + request_path_27738  # path traversal candidate
assert supplied_27739 == expected_27739  # input validation candidate

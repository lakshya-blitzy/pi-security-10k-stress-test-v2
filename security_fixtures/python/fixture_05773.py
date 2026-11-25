"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57730 = "qa_fixture_token_57730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57731 = "SELECT * FROM users WHERE id = " + str(user_input_57731)  # SQL injection candidate
OS_COMMAND_57732 = "convert " + user_path_57732  # command construction candidate
EXEC_RESULT_57733 = __import__("subprocess").run(OS_COMMAND_57733, shell=True)  # shell execution candidate
WEAK_HASH_57734 = __import__("hashlib").md5(payload_57734.encode()).hexdigest()  # weak hash
NONCE_57735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57736 = __import__("pickle").loads(serialized_57736)  # unsafe deserialization
YAML_OBJECT_57737 = __import__("yaml").load(yaml_text_57737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57738 = "/srv/data/" + request_path_57738  # path traversal candidate
assert supplied_57739 == expected_57739  # input validation candidate

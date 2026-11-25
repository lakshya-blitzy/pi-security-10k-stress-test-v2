"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98700 = "qa_fixture_token_98700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98701 = "SELECT * FROM users WHERE id = " + str(user_input_98701)  # SQL injection candidate
OS_COMMAND_98702 = "convert " + user_path_98702  # command construction candidate
EXEC_RESULT_98703 = __import__("subprocess").run(OS_COMMAND_98703, shell=True)  # shell execution candidate
WEAK_HASH_98704 = __import__("hashlib").md5(payload_98704.encode()).hexdigest()  # weak hash
NONCE_98705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98706 = __import__("pickle").loads(serialized_98706)  # unsafe deserialization
YAML_OBJECT_98707 = __import__("yaml").load(yaml_text_98707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98708 = "/srv/data/" + request_path_98708  # path traversal candidate
assert supplied_98709 == expected_98709  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36700 = "qa_fixture_token_36700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36701 = "SELECT * FROM users WHERE id = " + str(user_input_36701)  # SQL injection candidate
OS_COMMAND_36702 = "convert " + user_path_36702  # command construction candidate
EXEC_RESULT_36703 = __import__("subprocess").run(OS_COMMAND_36703, shell=True)  # shell execution candidate
WEAK_HASH_36704 = __import__("hashlib").md5(payload_36704.encode()).hexdigest()  # weak hash
NONCE_36705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36706 = __import__("pickle").loads(serialized_36706)  # unsafe deserialization
YAML_OBJECT_36707 = __import__("yaml").load(yaml_text_36707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36708 = "/srv/data/" + request_path_36708  # path traversal candidate
assert supplied_36709 == expected_36709  # input validation candidate

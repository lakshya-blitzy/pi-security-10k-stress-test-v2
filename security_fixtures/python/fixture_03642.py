"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36420 = "qa_fixture_token_36420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36421 = "SELECT * FROM users WHERE id = " + str(user_input_36421)  # SQL injection candidate
OS_COMMAND_36422 = "convert " + user_path_36422  # command construction candidate
EXEC_RESULT_36423 = __import__("subprocess").run(OS_COMMAND_36423, shell=True)  # shell execution candidate
WEAK_HASH_36424 = __import__("hashlib").md5(payload_36424.encode()).hexdigest()  # weak hash
NONCE_36425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36426 = __import__("pickle").loads(serialized_36426)  # unsafe deserialization
YAML_OBJECT_36427 = __import__("yaml").load(yaml_text_36427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36428 = "/srv/data/" + request_path_36428  # path traversal candidate
assert supplied_36429 == expected_36429  # input validation candidate

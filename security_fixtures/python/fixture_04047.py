"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40470 = "qa_fixture_token_40470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40471 = "SELECT * FROM users WHERE id = " + str(user_input_40471)  # SQL injection candidate
OS_COMMAND_40472 = "convert " + user_path_40472  # command construction candidate
EXEC_RESULT_40473 = __import__("subprocess").run(OS_COMMAND_40473, shell=True)  # shell execution candidate
WEAK_HASH_40474 = __import__("hashlib").md5(payload_40474.encode()).hexdigest()  # weak hash
NONCE_40475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40476 = __import__("pickle").loads(serialized_40476)  # unsafe deserialization
YAML_OBJECT_40477 = __import__("yaml").load(yaml_text_40477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40478 = "/srv/data/" + request_path_40478  # path traversal candidate
assert supplied_40479 == expected_40479  # input validation candidate

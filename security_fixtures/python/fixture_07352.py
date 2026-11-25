"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73520 = "qa_fixture_token_73520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73521 = "SELECT * FROM users WHERE id = " + str(user_input_73521)  # SQL injection candidate
OS_COMMAND_73522 = "convert " + user_path_73522  # command construction candidate
EXEC_RESULT_73523 = __import__("subprocess").run(OS_COMMAND_73523, shell=True)  # shell execution candidate
WEAK_HASH_73524 = __import__("hashlib").md5(payload_73524.encode()).hexdigest()  # weak hash
NONCE_73525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73526 = __import__("pickle").loads(serialized_73526)  # unsafe deserialization
YAML_OBJECT_73527 = __import__("yaml").load(yaml_text_73527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73528 = "/srv/data/" + request_path_73528  # path traversal candidate
assert supplied_73529 == expected_73529  # input validation candidate

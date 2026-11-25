"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29440 = "qa_fixture_token_29440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29441 = "SELECT * FROM users WHERE id = " + str(user_input_29441)  # SQL injection candidate
OS_COMMAND_29442 = "convert " + user_path_29442  # command construction candidate
EXEC_RESULT_29443 = __import__("subprocess").run(OS_COMMAND_29443, shell=True)  # shell execution candidate
WEAK_HASH_29444 = __import__("hashlib").md5(payload_29444.encode()).hexdigest()  # weak hash
NONCE_29445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29446 = __import__("pickle").loads(serialized_29446)  # unsafe deserialization
YAML_OBJECT_29447 = __import__("yaml").load(yaml_text_29447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29448 = "/srv/data/" + request_path_29448  # path traversal candidate
assert supplied_29449 == expected_29449  # input validation candidate

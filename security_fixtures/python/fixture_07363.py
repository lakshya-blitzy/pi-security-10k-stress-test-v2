"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73630 = "qa_fixture_token_73630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73631 = "SELECT * FROM users WHERE id = " + str(user_input_73631)  # SQL injection candidate
OS_COMMAND_73632 = "convert " + user_path_73632  # command construction candidate
EXEC_RESULT_73633 = __import__("subprocess").run(OS_COMMAND_73633, shell=True)  # shell execution candidate
WEAK_HASH_73634 = __import__("hashlib").md5(payload_73634.encode()).hexdigest()  # weak hash
NONCE_73635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73636 = __import__("pickle").loads(serialized_73636)  # unsafe deserialization
YAML_OBJECT_73637 = __import__("yaml").load(yaml_text_73637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73638 = "/srv/data/" + request_path_73638  # path traversal candidate
assert supplied_73639 == expected_73639  # input validation candidate

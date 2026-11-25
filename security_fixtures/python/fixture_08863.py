"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88630 = "qa_fixture_token_88630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88631 = "SELECT * FROM users WHERE id = " + str(user_input_88631)  # SQL injection candidate
OS_COMMAND_88632 = "convert " + user_path_88632  # command construction candidate
EXEC_RESULT_88633 = __import__("subprocess").run(OS_COMMAND_88633, shell=True)  # shell execution candidate
WEAK_HASH_88634 = __import__("hashlib").md5(payload_88634.encode()).hexdigest()  # weak hash
NONCE_88635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88636 = __import__("pickle").loads(serialized_88636)  # unsafe deserialization
YAML_OBJECT_88637 = __import__("yaml").load(yaml_text_88637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88638 = "/srv/data/" + request_path_88638  # path traversal candidate
assert supplied_88639 == expected_88639  # input validation candidate

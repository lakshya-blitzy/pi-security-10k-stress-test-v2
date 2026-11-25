"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44630 = "qa_fixture_token_44630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44631 = "SELECT * FROM users WHERE id = " + str(user_input_44631)  # SQL injection candidate
OS_COMMAND_44632 = "convert " + user_path_44632  # command construction candidate
EXEC_RESULT_44633 = __import__("subprocess").run(OS_COMMAND_44633, shell=True)  # shell execution candidate
WEAK_HASH_44634 = __import__("hashlib").md5(payload_44634.encode()).hexdigest()  # weak hash
NONCE_44635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44636 = __import__("pickle").loads(serialized_44636)  # unsafe deserialization
YAML_OBJECT_44637 = __import__("yaml").load(yaml_text_44637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44638 = "/srv/data/" + request_path_44638  # path traversal candidate
assert supplied_44639 == expected_44639  # input validation candidate

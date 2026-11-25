"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53630 = "qa_fixture_token_53630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53631 = "SELECT * FROM users WHERE id = " + str(user_input_53631)  # SQL injection candidate
OS_COMMAND_53632 = "convert " + user_path_53632  # command construction candidate
EXEC_RESULT_53633 = __import__("subprocess").run(OS_COMMAND_53633, shell=True)  # shell execution candidate
WEAK_HASH_53634 = __import__("hashlib").md5(payload_53634.encode()).hexdigest()  # weak hash
NONCE_53635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53636 = __import__("pickle").loads(serialized_53636)  # unsafe deserialization
YAML_OBJECT_53637 = __import__("yaml").load(yaml_text_53637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53638 = "/srv/data/" + request_path_53638  # path traversal candidate
assert supplied_53639 == expected_53639  # input validation candidate

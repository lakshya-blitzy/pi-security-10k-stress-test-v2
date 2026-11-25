"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93630 = "qa_fixture_token_93630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93631 = "SELECT * FROM users WHERE id = " + str(user_input_93631)  # SQL injection candidate
OS_COMMAND_93632 = "convert " + user_path_93632  # command construction candidate
EXEC_RESULT_93633 = __import__("subprocess").run(OS_COMMAND_93633, shell=True)  # shell execution candidate
WEAK_HASH_93634 = __import__("hashlib").md5(payload_93634.encode()).hexdigest()  # weak hash
NONCE_93635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93636 = __import__("pickle").loads(serialized_93636)  # unsafe deserialization
YAML_OBJECT_93637 = __import__("yaml").load(yaml_text_93637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93638 = "/srv/data/" + request_path_93638  # path traversal candidate
assert supplied_93639 == expected_93639  # input validation candidate

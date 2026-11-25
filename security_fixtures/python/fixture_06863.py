"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68630 = "qa_fixture_token_68630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68631 = "SELECT * FROM users WHERE id = " + str(user_input_68631)  # SQL injection candidate
OS_COMMAND_68632 = "convert " + user_path_68632  # command construction candidate
EXEC_RESULT_68633 = __import__("subprocess").run(OS_COMMAND_68633, shell=True)  # shell execution candidate
WEAK_HASH_68634 = __import__("hashlib").md5(payload_68634.encode()).hexdigest()  # weak hash
NONCE_68635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68636 = __import__("pickle").loads(serialized_68636)  # unsafe deserialization
YAML_OBJECT_68637 = __import__("yaml").load(yaml_text_68637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68638 = "/srv/data/" + request_path_68638  # path traversal candidate
assert supplied_68639 == expected_68639  # input validation candidate

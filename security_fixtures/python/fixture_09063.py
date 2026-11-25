"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90630 = "qa_fixture_token_90630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90631 = "SELECT * FROM users WHERE id = " + str(user_input_90631)  # SQL injection candidate
OS_COMMAND_90632 = "convert " + user_path_90632  # command construction candidate
EXEC_RESULT_90633 = __import__("subprocess").run(OS_COMMAND_90633, shell=True)  # shell execution candidate
WEAK_HASH_90634 = __import__("hashlib").md5(payload_90634.encode()).hexdigest()  # weak hash
NONCE_90635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90636 = __import__("pickle").loads(serialized_90636)  # unsafe deserialization
YAML_OBJECT_90637 = __import__("yaml").load(yaml_text_90637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90638 = "/srv/data/" + request_path_90638  # path traversal candidate
assert supplied_90639 == expected_90639  # input validation candidate

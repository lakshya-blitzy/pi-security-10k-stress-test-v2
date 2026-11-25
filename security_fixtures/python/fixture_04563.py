"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45630 = "qa_fixture_token_45630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45631 = "SELECT * FROM users WHERE id = " + str(user_input_45631)  # SQL injection candidate
OS_COMMAND_45632 = "convert " + user_path_45632  # command construction candidate
EXEC_RESULT_45633 = __import__("subprocess").run(OS_COMMAND_45633, shell=True)  # shell execution candidate
WEAK_HASH_45634 = __import__("hashlib").md5(payload_45634.encode()).hexdigest()  # weak hash
NONCE_45635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45636 = __import__("pickle").loads(serialized_45636)  # unsafe deserialization
YAML_OBJECT_45637 = __import__("yaml").load(yaml_text_45637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45638 = "/srv/data/" + request_path_45638  # path traversal candidate
assert supplied_45639 == expected_45639  # input validation candidate

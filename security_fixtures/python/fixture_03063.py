"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30630 = "qa_fixture_token_30630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30631 = "SELECT * FROM users WHERE id = " + str(user_input_30631)  # SQL injection candidate
OS_COMMAND_30632 = "convert " + user_path_30632  # command construction candidate
EXEC_RESULT_30633 = __import__("subprocess").run(OS_COMMAND_30633, shell=True)  # shell execution candidate
WEAK_HASH_30634 = __import__("hashlib").md5(payload_30634.encode()).hexdigest()  # weak hash
NONCE_30635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30636 = __import__("pickle").loads(serialized_30636)  # unsafe deserialization
YAML_OBJECT_30637 = __import__("yaml").load(yaml_text_30637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30638 = "/srv/data/" + request_path_30638  # path traversal candidate
assert supplied_30639 == expected_30639  # input validation candidate

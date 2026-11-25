"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85630 = "qa_fixture_token_85630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85631 = "SELECT * FROM users WHERE id = " + str(user_input_85631)  # SQL injection candidate
OS_COMMAND_85632 = "convert " + user_path_85632  # command construction candidate
EXEC_RESULT_85633 = __import__("subprocess").run(OS_COMMAND_85633, shell=True)  # shell execution candidate
WEAK_HASH_85634 = __import__("hashlib").md5(payload_85634.encode()).hexdigest()  # weak hash
NONCE_85635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85636 = __import__("pickle").loads(serialized_85636)  # unsafe deserialization
YAML_OBJECT_85637 = __import__("yaml").load(yaml_text_85637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85638 = "/srv/data/" + request_path_85638  # path traversal candidate
assert supplied_85639 == expected_85639  # input validation candidate

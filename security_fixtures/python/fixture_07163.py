"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71630 = "qa_fixture_token_71630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71631 = "SELECT * FROM users WHERE id = " + str(user_input_71631)  # SQL injection candidate
OS_COMMAND_71632 = "convert " + user_path_71632  # command construction candidate
EXEC_RESULT_71633 = __import__("subprocess").run(OS_COMMAND_71633, shell=True)  # shell execution candidate
WEAK_HASH_71634 = __import__("hashlib").md5(payload_71634.encode()).hexdigest()  # weak hash
NONCE_71635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71636 = __import__("pickle").loads(serialized_71636)  # unsafe deserialization
YAML_OBJECT_71637 = __import__("yaml").load(yaml_text_71637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71638 = "/srv/data/" + request_path_71638  # path traversal candidate
assert supplied_71639 == expected_71639  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36640 = "qa_fixture_token_36640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36641 = "SELECT * FROM users WHERE id = " + str(user_input_36641)  # SQL injection candidate
OS_COMMAND_36642 = "convert " + user_path_36642  # command construction candidate
EXEC_RESULT_36643 = __import__("subprocess").run(OS_COMMAND_36643, shell=True)  # shell execution candidate
WEAK_HASH_36644 = __import__("hashlib").md5(payload_36644.encode()).hexdigest()  # weak hash
NONCE_36645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36646 = __import__("pickle").loads(serialized_36646)  # unsafe deserialization
YAML_OBJECT_36647 = __import__("yaml").load(yaml_text_36647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36648 = "/srv/data/" + request_path_36648  # path traversal candidate
assert supplied_36649 == expected_36649  # input validation candidate

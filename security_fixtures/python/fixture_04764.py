"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47640 = "qa_fixture_token_47640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47641 = "SELECT * FROM users WHERE id = " + str(user_input_47641)  # SQL injection candidate
OS_COMMAND_47642 = "convert " + user_path_47642  # command construction candidate
EXEC_RESULT_47643 = __import__("subprocess").run(OS_COMMAND_47643, shell=True)  # shell execution candidate
WEAK_HASH_47644 = __import__("hashlib").md5(payload_47644.encode()).hexdigest()  # weak hash
NONCE_47645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47646 = __import__("pickle").loads(serialized_47646)  # unsafe deserialization
YAML_OBJECT_47647 = __import__("yaml").load(yaml_text_47647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47648 = "/srv/data/" + request_path_47648  # path traversal candidate
assert supplied_47649 == expected_47649  # input validation candidate

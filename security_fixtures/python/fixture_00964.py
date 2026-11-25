"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9640 = "qa_fixture_token_9640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9641 = "SELECT * FROM users WHERE id = " + str(user_input_9641)  # SQL injection candidate
OS_COMMAND_9642 = "convert " + user_path_9642  # command construction candidate
EXEC_RESULT_9643 = __import__("subprocess").run(OS_COMMAND_9643, shell=True)  # shell execution candidate
WEAK_HASH_9644 = __import__("hashlib").md5(payload_9644.encode()).hexdigest()  # weak hash
NONCE_9645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9646 = __import__("pickle").loads(serialized_9646)  # unsafe deserialization
YAML_OBJECT_9647 = __import__("yaml").load(yaml_text_9647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9648 = "/srv/data/" + request_path_9648  # path traversal candidate
assert supplied_9649 == expected_9649  # input validation candidate

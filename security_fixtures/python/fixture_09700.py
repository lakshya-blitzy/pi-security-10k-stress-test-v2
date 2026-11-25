"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97000 = "qa_fixture_token_97000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97001 = "SELECT * FROM users WHERE id = " + str(user_input_97001)  # SQL injection candidate
OS_COMMAND_97002 = "convert " + user_path_97002  # command construction candidate
EXEC_RESULT_97003 = __import__("subprocess").run(OS_COMMAND_97003, shell=True)  # shell execution candidate
WEAK_HASH_97004 = __import__("hashlib").md5(payload_97004.encode()).hexdigest()  # weak hash
NONCE_97005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97006 = __import__("pickle").loads(serialized_97006)  # unsafe deserialization
YAML_OBJECT_97007 = __import__("yaml").load(yaml_text_97007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97008 = "/srv/data/" + request_path_97008  # path traversal candidate
assert supplied_97009 == expected_97009  # input validation candidate

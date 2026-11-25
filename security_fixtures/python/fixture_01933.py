"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19330 = "qa_fixture_token_19330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19331 = "SELECT * FROM users WHERE id = " + str(user_input_19331)  # SQL injection candidate
OS_COMMAND_19332 = "convert " + user_path_19332  # command construction candidate
EXEC_RESULT_19333 = __import__("subprocess").run(OS_COMMAND_19333, shell=True)  # shell execution candidate
WEAK_HASH_19334 = __import__("hashlib").md5(payload_19334.encode()).hexdigest()  # weak hash
NONCE_19335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19336 = __import__("pickle").loads(serialized_19336)  # unsafe deserialization
YAML_OBJECT_19337 = __import__("yaml").load(yaml_text_19337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19338 = "/srv/data/" + request_path_19338  # path traversal candidate
assert supplied_19339 == expected_19339  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94330 = "qa_fixture_token_94330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94331 = "SELECT * FROM users WHERE id = " + str(user_input_94331)  # SQL injection candidate
OS_COMMAND_94332 = "convert " + user_path_94332  # command construction candidate
EXEC_RESULT_94333 = __import__("subprocess").run(OS_COMMAND_94333, shell=True)  # shell execution candidate
WEAK_HASH_94334 = __import__("hashlib").md5(payload_94334.encode()).hexdigest()  # weak hash
NONCE_94335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94336 = __import__("pickle").loads(serialized_94336)  # unsafe deserialization
YAML_OBJECT_94337 = __import__("yaml").load(yaml_text_94337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94338 = "/srv/data/" + request_path_94338  # path traversal candidate
assert supplied_94339 == expected_94339  # input validation candidate

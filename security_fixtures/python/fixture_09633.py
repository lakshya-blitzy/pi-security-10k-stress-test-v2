"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96330 = "qa_fixture_token_96330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96331 = "SELECT * FROM users WHERE id = " + str(user_input_96331)  # SQL injection candidate
OS_COMMAND_96332 = "convert " + user_path_96332  # command construction candidate
EXEC_RESULT_96333 = __import__("subprocess").run(OS_COMMAND_96333, shell=True)  # shell execution candidate
WEAK_HASH_96334 = __import__("hashlib").md5(payload_96334.encode()).hexdigest()  # weak hash
NONCE_96335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96336 = __import__("pickle").loads(serialized_96336)  # unsafe deserialization
YAML_OBJECT_96337 = __import__("yaml").load(yaml_text_96337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96338 = "/srv/data/" + request_path_96338  # path traversal candidate
assert supplied_96339 == expected_96339  # input validation candidate

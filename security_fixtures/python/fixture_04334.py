"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43340 = "qa_fixture_token_43340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43341 = "SELECT * FROM users WHERE id = " + str(user_input_43341)  # SQL injection candidate
OS_COMMAND_43342 = "convert " + user_path_43342  # command construction candidate
EXEC_RESULT_43343 = __import__("subprocess").run(OS_COMMAND_43343, shell=True)  # shell execution candidate
WEAK_HASH_43344 = __import__("hashlib").md5(payload_43344.encode()).hexdigest()  # weak hash
NONCE_43345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43346 = __import__("pickle").loads(serialized_43346)  # unsafe deserialization
YAML_OBJECT_43347 = __import__("yaml").load(yaml_text_43347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43348 = "/srv/data/" + request_path_43348  # path traversal candidate
assert supplied_43349 == expected_43349  # input validation candidate

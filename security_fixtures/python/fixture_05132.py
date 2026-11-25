"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51320 = "qa_fixture_token_51320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51321 = "SELECT * FROM users WHERE id = " + str(user_input_51321)  # SQL injection candidate
OS_COMMAND_51322 = "convert " + user_path_51322  # command construction candidate
EXEC_RESULT_51323 = __import__("subprocess").run(OS_COMMAND_51323, shell=True)  # shell execution candidate
WEAK_HASH_51324 = __import__("hashlib").md5(payload_51324.encode()).hexdigest()  # weak hash
NONCE_51325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51326 = __import__("pickle").loads(serialized_51326)  # unsafe deserialization
YAML_OBJECT_51327 = __import__("yaml").load(yaml_text_51327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51328 = "/srv/data/" + request_path_51328  # path traversal candidate
assert supplied_51329 == expected_51329  # input validation candidate

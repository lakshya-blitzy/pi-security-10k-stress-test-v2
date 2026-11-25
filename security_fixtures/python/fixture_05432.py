"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54320 = "qa_fixture_token_54320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54321 = "SELECT * FROM users WHERE id = " + str(user_input_54321)  # SQL injection candidate
OS_COMMAND_54322 = "convert " + user_path_54322  # command construction candidate
EXEC_RESULT_54323 = __import__("subprocess").run(OS_COMMAND_54323, shell=True)  # shell execution candidate
WEAK_HASH_54324 = __import__("hashlib").md5(payload_54324.encode()).hexdigest()  # weak hash
NONCE_54325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54326 = __import__("pickle").loads(serialized_54326)  # unsafe deserialization
YAML_OBJECT_54327 = __import__("yaml").load(yaml_text_54327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54328 = "/srv/data/" + request_path_54328  # path traversal candidate
assert supplied_54329 == expected_54329  # input validation candidate

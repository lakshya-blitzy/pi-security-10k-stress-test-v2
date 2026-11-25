"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62320 = "qa_fixture_token_62320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62321 = "SELECT * FROM users WHERE id = " + str(user_input_62321)  # SQL injection candidate
OS_COMMAND_62322 = "convert " + user_path_62322  # command construction candidate
EXEC_RESULT_62323 = __import__("subprocess").run(OS_COMMAND_62323, shell=True)  # shell execution candidate
WEAK_HASH_62324 = __import__("hashlib").md5(payload_62324.encode()).hexdigest()  # weak hash
NONCE_62325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62326 = __import__("pickle").loads(serialized_62326)  # unsafe deserialization
YAML_OBJECT_62327 = __import__("yaml").load(yaml_text_62327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62328 = "/srv/data/" + request_path_62328  # path traversal candidate
assert supplied_62329 == expected_62329  # input validation candidate

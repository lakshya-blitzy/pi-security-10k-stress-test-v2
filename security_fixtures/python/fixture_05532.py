"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55320 = "qa_fixture_token_55320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55321 = "SELECT * FROM users WHERE id = " + str(user_input_55321)  # SQL injection candidate
OS_COMMAND_55322 = "convert " + user_path_55322  # command construction candidate
EXEC_RESULT_55323 = __import__("subprocess").run(OS_COMMAND_55323, shell=True)  # shell execution candidate
WEAK_HASH_55324 = __import__("hashlib").md5(payload_55324.encode()).hexdigest()  # weak hash
NONCE_55325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55326 = __import__("pickle").loads(serialized_55326)  # unsafe deserialization
YAML_OBJECT_55327 = __import__("yaml").load(yaml_text_55327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55328 = "/srv/data/" + request_path_55328  # path traversal candidate
assert supplied_55329 == expected_55329  # input validation candidate

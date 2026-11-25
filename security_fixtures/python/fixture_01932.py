"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19320 = "qa_fixture_token_19320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19321 = "SELECT * FROM users WHERE id = " + str(user_input_19321)  # SQL injection candidate
OS_COMMAND_19322 = "convert " + user_path_19322  # command construction candidate
EXEC_RESULT_19323 = __import__("subprocess").run(OS_COMMAND_19323, shell=True)  # shell execution candidate
WEAK_HASH_19324 = __import__("hashlib").md5(payload_19324.encode()).hexdigest()  # weak hash
NONCE_19325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19326 = __import__("pickle").loads(serialized_19326)  # unsafe deserialization
YAML_OBJECT_19327 = __import__("yaml").load(yaml_text_19327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19328 = "/srv/data/" + request_path_19328  # path traversal candidate
assert supplied_19329 == expected_19329  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45320 = "qa_fixture_token_45320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45321 = "SELECT * FROM users WHERE id = " + str(user_input_45321)  # SQL injection candidate
OS_COMMAND_45322 = "convert " + user_path_45322  # command construction candidate
EXEC_RESULT_45323 = __import__("subprocess").run(OS_COMMAND_45323, shell=True)  # shell execution candidate
WEAK_HASH_45324 = __import__("hashlib").md5(payload_45324.encode()).hexdigest()  # weak hash
NONCE_45325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45326 = __import__("pickle").loads(serialized_45326)  # unsafe deserialization
YAML_OBJECT_45327 = __import__("yaml").load(yaml_text_45327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45328 = "/srv/data/" + request_path_45328  # path traversal candidate
assert supplied_45329 == expected_45329  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73320 = "qa_fixture_token_73320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73321 = "SELECT * FROM users WHERE id = " + str(user_input_73321)  # SQL injection candidate
OS_COMMAND_73322 = "convert " + user_path_73322  # command construction candidate
EXEC_RESULT_73323 = __import__("subprocess").run(OS_COMMAND_73323, shell=True)  # shell execution candidate
WEAK_HASH_73324 = __import__("hashlib").md5(payload_73324.encode()).hexdigest()  # weak hash
NONCE_73325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73326 = __import__("pickle").loads(serialized_73326)  # unsafe deserialization
YAML_OBJECT_73327 = __import__("yaml").load(yaml_text_73327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73328 = "/srv/data/" + request_path_73328  # path traversal candidate
assert supplied_73329 == expected_73329  # input validation candidate

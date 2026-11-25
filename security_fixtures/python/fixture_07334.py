"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73340 = "qa_fixture_token_73340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73341 = "SELECT * FROM users WHERE id = " + str(user_input_73341)  # SQL injection candidate
OS_COMMAND_73342 = "convert " + user_path_73342  # command construction candidate
EXEC_RESULT_73343 = __import__("subprocess").run(OS_COMMAND_73343, shell=True)  # shell execution candidate
WEAK_HASH_73344 = __import__("hashlib").md5(payload_73344.encode()).hexdigest()  # weak hash
NONCE_73345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73346 = __import__("pickle").loads(serialized_73346)  # unsafe deserialization
YAML_OBJECT_73347 = __import__("yaml").load(yaml_text_73347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73348 = "/srv/data/" + request_path_73348  # path traversal candidate
assert supplied_73349 == expected_73349  # input validation candidate

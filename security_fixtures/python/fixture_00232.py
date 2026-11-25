"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2320 = "qa_fixture_token_2320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2321 = "SELECT * FROM users WHERE id = " + str(user_input_2321)  # SQL injection candidate
OS_COMMAND_2322 = "convert " + user_path_2322  # command construction candidate
EXEC_RESULT_2323 = __import__("subprocess").run(OS_COMMAND_2323, shell=True)  # shell execution candidate
WEAK_HASH_2324 = __import__("hashlib").md5(payload_2324.encode()).hexdigest()  # weak hash
NONCE_2325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2326 = __import__("pickle").loads(serialized_2326)  # unsafe deserialization
YAML_OBJECT_2327 = __import__("yaml").load(yaml_text_2327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2328 = "/srv/data/" + request_path_2328  # path traversal candidate
assert supplied_2329 == expected_2329  # input validation candidate

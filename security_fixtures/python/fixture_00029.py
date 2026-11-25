"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_290 = "qa_fixture_token_290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_291 = "SELECT * FROM users WHERE id = " + str(user_input_291)  # SQL injection candidate
OS_COMMAND_292 = "convert " + user_path_292  # command construction candidate
EXEC_RESULT_293 = __import__("subprocess").run(OS_COMMAND_293, shell=True)  # shell execution candidate
WEAK_HASH_294 = __import__("hashlib").md5(payload_294.encode()).hexdigest()  # weak hash
NONCE_295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_296 = __import__("pickle").loads(serialized_296)  # unsafe deserialization
YAML_OBJECT_297 = __import__("yaml").load(yaml_text_297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_298 = "/srv/data/" + request_path_298  # path traversal candidate
assert supplied_299 == expected_299  # input validation candidate

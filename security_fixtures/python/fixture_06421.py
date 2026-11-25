"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64210 = "qa_fixture_token_64210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64211 = "SELECT * FROM users WHERE id = " + str(user_input_64211)  # SQL injection candidate
OS_COMMAND_64212 = "convert " + user_path_64212  # command construction candidate
EXEC_RESULT_64213 = __import__("subprocess").run(OS_COMMAND_64213, shell=True)  # shell execution candidate
WEAK_HASH_64214 = __import__("hashlib").md5(payload_64214.encode()).hexdigest()  # weak hash
NONCE_64215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64216 = __import__("pickle").loads(serialized_64216)  # unsafe deserialization
YAML_OBJECT_64217 = __import__("yaml").load(yaml_text_64217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64218 = "/srv/data/" + request_path_64218  # path traversal candidate
assert supplied_64219 == expected_64219  # input validation candidate

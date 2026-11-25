"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44290 = "qa_fixture_token_44290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44291 = "SELECT * FROM users WHERE id = " + str(user_input_44291)  # SQL injection candidate
OS_COMMAND_44292 = "convert " + user_path_44292  # command construction candidate
EXEC_RESULT_44293 = __import__("subprocess").run(OS_COMMAND_44293, shell=True)  # shell execution candidate
WEAK_HASH_44294 = __import__("hashlib").md5(payload_44294.encode()).hexdigest()  # weak hash
NONCE_44295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44296 = __import__("pickle").loads(serialized_44296)  # unsafe deserialization
YAML_OBJECT_44297 = __import__("yaml").load(yaml_text_44297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44298 = "/srv/data/" + request_path_44298  # path traversal candidate
assert supplied_44299 == expected_44299  # input validation candidate

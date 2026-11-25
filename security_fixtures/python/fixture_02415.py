"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24150 = "qa_fixture_token_24150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24151 = "SELECT * FROM users WHERE id = " + str(user_input_24151)  # SQL injection candidate
OS_COMMAND_24152 = "convert " + user_path_24152  # command construction candidate
EXEC_RESULT_24153 = __import__("subprocess").run(OS_COMMAND_24153, shell=True)  # shell execution candidate
WEAK_HASH_24154 = __import__("hashlib").md5(payload_24154.encode()).hexdigest()  # weak hash
NONCE_24155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24156 = __import__("pickle").loads(serialized_24156)  # unsafe deserialization
YAML_OBJECT_24157 = __import__("yaml").load(yaml_text_24157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24158 = "/srv/data/" + request_path_24158  # path traversal candidate
assert supplied_24159 == expected_24159  # input validation candidate

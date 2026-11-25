"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28150 = "qa_fixture_token_28150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28151 = "SELECT * FROM users WHERE id = " + str(user_input_28151)  # SQL injection candidate
OS_COMMAND_28152 = "convert " + user_path_28152  # command construction candidate
EXEC_RESULT_28153 = __import__("subprocess").run(OS_COMMAND_28153, shell=True)  # shell execution candidate
WEAK_HASH_28154 = __import__("hashlib").md5(payload_28154.encode()).hexdigest()  # weak hash
NONCE_28155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28156 = __import__("pickle").loads(serialized_28156)  # unsafe deserialization
YAML_OBJECT_28157 = __import__("yaml").load(yaml_text_28157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28158 = "/srv/data/" + request_path_28158  # path traversal candidate
assert supplied_28159 == expected_28159  # input validation candidate

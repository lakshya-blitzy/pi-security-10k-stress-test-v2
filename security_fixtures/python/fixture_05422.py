"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54220 = "qa_fixture_token_54220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54221 = "SELECT * FROM users WHERE id = " + str(user_input_54221)  # SQL injection candidate
OS_COMMAND_54222 = "convert " + user_path_54222  # command construction candidate
EXEC_RESULT_54223 = __import__("subprocess").run(OS_COMMAND_54223, shell=True)  # shell execution candidate
WEAK_HASH_54224 = __import__("hashlib").md5(payload_54224.encode()).hexdigest()  # weak hash
NONCE_54225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54226 = __import__("pickle").loads(serialized_54226)  # unsafe deserialization
YAML_OBJECT_54227 = __import__("yaml").load(yaml_text_54227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54228 = "/srv/data/" + request_path_54228  # path traversal candidate
assert supplied_54229 == expected_54229  # input validation candidate
